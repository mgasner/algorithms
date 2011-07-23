import array
import random
import math
import numpy as np

"""
MCMC via the Metropolis algorithm for simple substitution ciphers, after Percy Diaconis, The Markov Chain Monte Carlo Revolution, Bull. AMS, 2009
"""

unknown = "?"

def get_alphabet_from_string(s):
  D = {}
  for ch in s:
    if not(ch in D):
      D[ch] = ch;
  return D
  
def transition_matrix(string, alphabet = None):
  if alphabet == None:
    alphabet = get_alphabet_from_string(string)
  matrix = dict()
  for i in alphabet:
    for j in alphabet:
      matrix[i+j] = float(1)
  for i in range(len(string) - 1):
    matrix[string[i] + string[i+1]] = matrix[string[i] + string[i+1]] + 1
  for i in alphabet:
    for j in alphabet:
      matrix[i + j] = matrix[i + j] / len(string)
      matrix[i + j] = np.log2(matrix[i + j])
  return matrix

def make_cipher(alphabet):
  keys = alphabet.keys()
  permutation = random.sample(keys, len(keys))
  cipher = dict()
  i = 0
  for key in alphabet.keys():
    cipher[key] = permutation[i]
    i = i + 1
  return cipher

def flip_weighted_coin(w):
  return random.random() < w

class Corpus:
  def __init__(self, filename, alphabet = None):
    with open(filename) as f:
      text = f.read()
      print(len(text))
      if alphabet == None:
        self.alphabet = get_alphabet_from_string(text)
      else:
        self.alphabet = alphabet
      self.transition = transition_matrix(text, self.alphabet)
  def score(self, text):
    s = 0;
    for i in range(len(text) - 2):
      t = self.transition[text[i] + text[i + 1]]
      s = s + t
    return s
      
class SubstitutionCipher:
  def __init__(self, alphabet = None):
    if alphabet != None:
      self.cipher = make_cipher(alphabet)
    
  def encode(self, plaintext):
    ciphertext = ""
    for ch in plaintext:
      try:
        ciphertext = ciphertext + self.cipher[ch]
      except:
        ciphertext = ciphertext + unknown
    return ciphertext
    
  def decode(self, ciphertext):
    plaintext = ""
    for ch in ciphertext:
      try:
        for key in self.cipher.keys():
          if self.cipher[key] == ch:
            plaintext = plaintext + key
            break
          else:
            pass
      except:
        plaintext = plaintext + unknown
    return plaintext

class MCMC:
  def __init__(self, guess, plausibility, propose):
    self.sample = guess
    self.plausibility = plausibility
    self.pl = self.plausibility(guess)
    self.propose = propose
    
  def step(self):
    sample = self.sample
    proposal = self.propose(sample)
    proposal_plausibility = self.plausibility(proposal)
    sample_plausibility = self.pl
    print(sample_plausibility)
    if proposal_plausibility >= sample_plausibility:
      self.sample = proposal
      self.pl = proposal_plausibility
    else:
      flip = flip_weighted_coin(math.exp(proposal_plausibility - sample_plausibility))
      if flip:
        print ("flipped!", math.exp(proposal_plausibility - sample_plausibility))
        self.sample = proposal
        self.pl = proposal_plausibility      
  def run(self, burnin, stride, n):
    for i in range(burnin):
      self.step()
      
    for i in range(n):
      for j in range(stride):
        self.step()
      log(i, self.sample.decode(plaintext), self.pl)
      

def permute_encoding(c):
  a = SubstitutionCipher()
  a.cipher = dict()
  for key in c.cipher.keys():
    a.cipher[key] = c.cipher[key]
  keys = random.sample(a.cipher.keys(), 2)
  i = a.cipher[keys[0]]
  a.cipher[keys[0]] = a.cipher[keys[1]]
  a.cipher[keys[1]] = i
  return a
  
plaintext = "gallia est omnis divisa in partes tres quarum unam incolunt belgae aliam aquitani tertiam qui ipsorum lingua celtae nostra galli appellantur hi omnes lingua institutis legibus inter se differunt gallos ab aquitanis garumna flumen a belgis matrona et sequana dividit horum omnium fortissimi sunt belgae propterea quod a cultu atque humanitate provinciae longissime absunt minimeque ad eos mercatores saepe commeant atque ea quae ad effeminandos animos pertinent important proximique sunt germanis qui trans rhenum incolunt quibuscum continenter bellum gerunt qua de causa helvetii quoque reliquos gallos virtute praecedunt quod fere cotidianis proeliis cum germanis contendunt cum aut suis finibus eos prohibent aut ipsi in eorum finibus bellum gerunt eorum una pars quam gallos obtinere dictum est initium capit a flumine rhodano continetur garumna flumine oceano finibus belgarum attingit etiam ab sequanis et helvetiis flumen rhenum vergit ad septentriones belgae ab extremis galliae finibus oriuntur pertinent ad inferiorem partem fluminis rheni spectant in septentrionem et orientem solem aquitania a garumna flumine ad pyrenaeos montes et eam partem oceani quae est ad hispaniam pertinet spectat inter occasum solis et septentriones"

corpus = Corpus("/Users/maxgasner/algorithms/mcmc/caesar.txt")
cipher = SubstitutionCipher(corpus.alphabet)
ciphertext = cipher.encode(plaintext)

def log(*args):
  sep = ""
  with open("/Users/maxgasner/algorithms/mcmc/log.txt", "a") as f:
    f.write(sep.join(str(args)))
    f.write("\n")

def plausibility(cipher):
  return corpus.score(cipher.decode(ciphertext))
  
print(corpus.score(plaintext))
#print(corpus.transition)
for i in range(100):
  mcmc = MCMC(SubstitutionCipher(corpus.alphabet), plausibility, permute_encoding)
  mcmc.run(0, 60000, 1)
