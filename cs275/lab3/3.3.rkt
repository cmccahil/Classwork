#lang racket

(define dot-product
  (lambda (vec1 vec2)
    (cond
      ((null? vec1) 0)
      (else (apply + (map * vec1 vec2))))))