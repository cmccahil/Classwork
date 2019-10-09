#lang racket
(define list-of-ints?
  (lambda(y)
    (cond
      [(null? y) #t]
      [(integer? (car y)) (list-of-ints? (cdr y))]
      [else #f])))
                 