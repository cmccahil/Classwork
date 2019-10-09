#lang racket
(define atom?
  (lambda(y)
    (cond
      [(null? y)#f]
      [(list? y)#f]
      [else #t])))

(define list-of-same2
  (lambda(pred)
    (lambda(y)
      (cond
        [(null? y) #t]
        [(pred (car y)) ((list-of-same2 pred)(cdr y))]
        [else #f]))))