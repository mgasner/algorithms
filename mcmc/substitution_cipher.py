import array
import random

"""
MCMC for simple substitution ciphers, after Percy Diaconis, The Markov Chain Monte Carlo Revolution, Bull. AMS, 2009
"""

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
    matrix[i] = dict()
    for j in alphabet:
      matrix[i][j] = 0
  for i in range(len(string) - 1):
    matrix[string[i]][string[i + 1]] = matrix[string[i]][string[i + 1]] + 1
  return matrix

def make_cipher(alphabet):
  keys = alphabet.keys()
  permutation = random.sample(keys, len(keys))
  cipher = dict()
  for i in range(len(alphabet)):
    cipher[alphabet[i]] = permutation[i]
  return cipher

class Corpus:
  def __init__(self, filename, alphabet = None):
    with open(filename).read() as f:
      if alphabet == None:
        self.alphabet = get_alphabet_from_string(f)
      else:
        self.alphabet = alphabet
      self.transition_matrix = transition_matrix(f, self.alphabet)

  
class SubstitutionCipher:
  def __init__(self, alphabet):
    self.cipher = make_cipher(alphabet)
  def encode(plaintext):
  def decode(ciphertext):

class MCMC:



def make_substitution_cipher(s, D = get_dictionary_from_string(s)):
  keys = D.keys()
  cipher = random.sample(keys, len(keys))
  i = 0
  for ch in D:
    D[ch] = cipher[i]
    i = i + 1
  return D
  
def permute_values(D):
  keys = random.sample(D.keys(), 2)
  i = D[keys[0]]
  D[keys[0]] = D[keys[1]]
  D[keys[1]] = i
  return D

def encode(s):
  cipher = make_substitution_cipher(s)

def plausibility(M, f, s):
  

def guess_initial_code

def permute_code

def mcmc(f, x, step, P, n, stride):


def decode:
def calculate_transition_matrix(S):
  
  
plaintext = "We have all read a statement, (the authenticity of which I take leave to doubt entirely, for upon what calculations I should like to know is it founded?)--we have all, I say, been favoured by perusing a remark, that when the times and necessities of the world call for a Man, that individual is found. Thus at the French Revolution (which the reader will be pleased to have introduced so early), when it was requisite to administer a corrective dose to the nation, Robespierre was found; a most foul and nauseous dose indeed, and swallowed eagerly by the patient, greatly to the latter's ultimate advantage: thus, when it became necessary to kick John Bull out of America, Mr. Washington stepped forward, and performed that job to satisfaction: thus, when the Earl of Aldborough was unwell, Professor Holloway appeared with his pills, and cured his lordship, as per advertisement, &c. &c.. Numberless instances might be adduced to show that when a nation is in great want, the relief is at hand; just as in the Pantomime (that microcosm) where when CLOWN wants anything--a warming-pan, a pump-handle, a goose, or a lady's tippet--a fellow comes sauntering out from behind the side-scenes with the very article in question."
