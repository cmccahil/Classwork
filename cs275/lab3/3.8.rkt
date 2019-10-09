#lang racket

(define sum
  (lambda (L)
    (cond
      [(null? L) 0]
      [(number? L) L]
      [else (apply + (map sum L))])))