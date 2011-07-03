(define (naive-polynomial-eval coeffs x)
  (define (exp b n)
    (if (= n 0)
        1
        (* b (exp b (- n 1)))))
  (define (naive-polynomial-eval-help coeffs x i acc)
    (if (= (length coeffs) i)
        acc
        (naive-polynomial-eval-help coeffs x (+ i 1) (+ acc (* (list-ref coeffs i) (exp x i))))))
  (naive-polynomial-eval-help coeffs x 0 0))