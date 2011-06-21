(define (take n xs)
  (let loop ((n n) (xs xs) (ys '()))
    (if (or (zero? n) (null? xs))
      (reverse ys)
      (loop (- n 1) (cdr xs) (cons (car xs) ys)))))
      
(define (drop n xs)
  (let loop ((n n) (xs xs))
    (if (or (zero? n) (null? xs))
        xs
        (loop (- n 1) (cdr xs)))))

(define (merge-sort xs)
  (define (merge as bs)
    (let loop ((x (length as)) (y (length bs)) (as as) (bs bs) (ys '()))
      (cond ((zero? x) (append ys bs))
            ((zero? y) (append ys as))
            ((< (car as) (car bs)) (loop (- x 1) y (cdr as) bs (append ys (list (car as)))))
            (else (loop x (- y 1) as (cdr bs) (append ys (list (car bs))))))))
  (let ((len (length xs)))
    (if (> len 1)
      (let ((n (floor (/ len 2))))
        (merge (merge-sort (take n xs))
               (merge-sort (drop n xs))))
      xs)))