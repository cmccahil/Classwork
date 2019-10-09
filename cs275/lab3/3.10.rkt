#lang racket
(define atom? (lambda (x)
                (not (list? x))))

(define myOr (lambda args
  (cond
    [(null? args) #f]
    [(car args) #t]
    [else (apply myOr (cdr args))])))

(define element-of?
  (lambda (a L)
    (letrec ([h (lambda (x)
                  (cond
                    [(null? x) #f]
                    [(atom? x) (eq? x a)]
                    [else (apply myOr (map h x))]))])
      (h L))))
     