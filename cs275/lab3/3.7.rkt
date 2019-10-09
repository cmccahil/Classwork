#lang racket

(define atom? (lambda (x)
                (not (list? x))))

(define flatten
  (lambda (L)
    (cond
      [(null? L) null]
      ;[else (cdr L)])))
      [(atom? L) (list L)]
      [else (apply append (map flatten L))])))