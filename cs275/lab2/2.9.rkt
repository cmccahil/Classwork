#lang racket

(define max
  (letrec([max-a (lambda (lat acc)
                   (cond
                     [(null? lat) acc]
                     [(> (car lat) acc) (max-a (cdr lat) (car lat))]
                     [else (max-a (cdr lat) acc)]))])
    (lambda (lat) (max-a lat 0))))