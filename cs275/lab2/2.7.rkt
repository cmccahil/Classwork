#lang racket

(define length
  (letrec([length-a (lambda (lat acc)
                      (cond
                        [(null? lat) acc]
                        [else (length-a (cdr lat) (+ 1 acc))]))])
    (lambda (lat) (length-a lat 0))))