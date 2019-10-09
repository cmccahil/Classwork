#lang racket
(define atom? (lambda (x)
                (not (list? x))))

(define apply-to
  (lambda (f L)
    (cond
      [(null? L) null]
      [(atom? L) (f L)]
      [else (map(lambda(x)(apply-to f x))L)])))
