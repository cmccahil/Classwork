#lang racket
(define duplicate
  (lambda(n exp)
    (cond
      [(= n 0) null]
      [else(cons exp (duplicate (- n 1) exp))])))