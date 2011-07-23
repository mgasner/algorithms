(define (make-matrix n m)
  (let ((mat (make-vector n))) 
    (let loop ((i 0))
      (if (= i n)
          mat
          (begin
            (vector-set! mat i (make-vector m))
            (loop (+ i 1)))))))
            
(define (nrows mat)
  (vector-length mat))

(define (ncols mat)
  (vector-length (vector-ref mat 0)))

(define (get-matrix-entry mat i j)
  (vector-ref (vector-ref mat i) j))
  
(define (set-matrix-entry! mat i j val)
  (vector-set! (vector-ref mat i) j val))

(define (list->matrix l)
  (let ((n (length l)) (m (length (list-ref l 0))))
    (let ((mat (make-matrix n m)))
      (let loop ((i 0) (j 0))
        (if (= i n)
            mat
            (if (= j n)
                (loop (+ i 1) 0)
                (begin
                  (set-matrix-entry! mat i j (list-ref (list-ref l i) j))
                  (loop i (+ j 1)))))))))

(define (matrix-binary-elementwise-operation a b f)
  (let* ((n (nrows a)) (m (ncols a)) (c (make-matrix n m)))
    (let loop ((i 0) (j 0))
      (if (= i n)
          c
          (if (= j m)
              (loop (+ i 1) 0)
              (begin (set-matrix-entry! c i j
                       (f (get-matrix-entry a i j)
                          (get-matrix-entry b i j)))
                     (loop i (+ j 1))))))))

(define (matrix-add a b) (matrix-binary-elementwise-operation a b +))
(define (matrix-sub a b) (matrix-binary-elementwise-operation a b -))

(define (square-matrix-multiply a b)
  (let* ((n (nrows a)) (c (make-matrix n n)))
    (let loop ((i 0) (j 0) (k 0))
      (if (= i n)
          c
          (if (= j n)
              (loop (+ i 1) 0 k)
              (if (= k n)
                  (loop i (+ j 1) 0)
                  (begin (set-matrix-entry! c i j (+ (get-matrix-entry c i j) (* (get-matrix-entry a i k) (get-matrix-entry b k j))))
                  (loop i j (+ k 1)))))))))
                  
(define (square-matrix-multiply-recursive a b)
  (let* ((n (nrows a)) (c (make-matrix n n))
  
; strassen's method
; divide the input and output matrices into n/2 x n/2 submatrices
; create ten matrices each of which is n/2 * n/2
; recursively compute seven matrix products P1 - P7

(define (square-matrix-multiply-recursive a b a_m a_n b_m b_n)
  (let* ((n (nrows a)) (c (make-matrix n n)))
    (if (= n 1)
        (begin
          (set-matrix-entry! c 1 1 (* (get-matrix-entry a 1 1)
            (get-matrix-entry b 1 1)))
          c)
        ()
        