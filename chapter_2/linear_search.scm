(define (linear-search list key)
  (define (linear-search-help list key index)
    (cond
      ((null? list) list)
      ((eq? (car list) key) index)
      (else (linear-search-help (cdr list) key (+ index 1)))))
  (linear-search-help list key 0))