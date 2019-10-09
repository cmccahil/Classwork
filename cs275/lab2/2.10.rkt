#lang racket

(define index
  (letrec([index-a (lambda (a lat acc)
                     (cond
                       [(null? lat) -1]
                       [(eq? a (car lat)) acc]
                       [else (index-a a (cdr lat) (+ 1 acc))]))])
    (lambda (a lat) (index-a a lat 0))))