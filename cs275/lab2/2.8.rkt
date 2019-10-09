#lang racket

(define count
  (letrec([count-a (lambda (a lat acc)
                     (cond
                       [(null? lat) acc]
                       [(eq? a (car lat)) (count-a a (cdr lat) (+ 1 acc))]
                       [else (count-a a (cdr lat) acc)]))])
    (lambda (a lat) (count-a a lat 0))))