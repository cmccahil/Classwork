#lang racket
(define count 0)

(define rember-pair
  (lambda(a lat)
    (cond
      [(null? lat) null]
      [(and(eq? a (car lat)) (null? (cdr lat))) (cons(car lat) (rember-pair a (cdr lat)))]
      [(and(eq? a (car lat)) (eq? a (cadr lat))) (rember-pair a (cdr (cdr lat)))]
      [else (cons(car lat) (rember-pair a (cdr lat)))])))