(define (memoize f)
  (let ((memo (make-hash)))
    (lambda args
      (if (hash-has-key? memo args)
          (hash-ref memo args)
          (begin
            (let ((r (apply f args)))
              (hash-set! memo args r)
              r))))))