#lang racket
(define timeSeen 0)

(define rember2
  (lambda(a lat)
    (cond
      [(null? lat) (set! timeSeen 0) null]
      [(and(eq? a (car lat))(= 1 timeSeen)) (set! timeSeen (+ 1 timeSeen)) (rember2 a (cdr lat))]
      [(eq? a (car lat)) (set! timeSeen (+ 1 timeSeen)) (cons (car lat)(rember2 a (cdr lat)))]
      [else (cons(car lat) (rember2 a (cdr lat)))])))
