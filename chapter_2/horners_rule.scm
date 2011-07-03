(define (horners-rule coeffs x)
  (if (null? coeffs)
      0
      (+ (car coeffs) (* x (horners-rule (cdr coeffs) x)))))