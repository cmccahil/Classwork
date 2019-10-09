#lang racket

(define addvec
  (lambda (vec1 vec2)
    (cond
      [(null? vec1) null]
      [else (cons(+ (car vec1) (car vec2)) (addvec (cdr vec1) (cdr vec2)))])))