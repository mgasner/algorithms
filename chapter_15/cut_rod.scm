(define (cut-rod p n)
  (if (= n 0)
      0
      (let ((q (vector-ref p 0)))
        (let loop ((i 0))
          (if (= i n)
              q
              (begin
                (set! q (max q (+ (vector-ref p i) (cut-rod p (- n i)))))
                (loop (+ i 1))))))))
            