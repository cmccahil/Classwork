#lang racket
(define num 0)
(define return null)

(define index
  (lambda(a lat)
    (cond
      ((null? lat) -1)
      ((eq? a (car lat)) (set! return num) (set! num 0) return)
      [else (set! num (+ num 1)) (index a (cdr lat))])))