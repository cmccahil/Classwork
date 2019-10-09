#lang racket
(define number null)
(define return null)

(define largest
  (lambda(lat)
    (cond
      [(null? lat) (set! return number) (set! number null) return]
      [(null? number) (set! number (car lat)) (largest (cdr lat))]
      [(> (car lat) number) (set! number (car lat)) (largest (cdr lat))]
      [else (largest (cdr lat))])))