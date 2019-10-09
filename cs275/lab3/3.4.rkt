#lang racket

(define dot-row
  (lambda (vec mat)
    (cond
      [(null? mat) null]
      [else (cons(apply + (map * vec (car mat))) (dot-row vec (cdr mat)))])))