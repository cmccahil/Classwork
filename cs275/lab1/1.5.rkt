#lang racket
(define atom?
  (lambda(y)
    (cond
      [(null? y)#f]
      [(list? y)#f]
      [else #t])))

(define list-of-same?
  (lambda(pred x)
    (cond
      ((null? x) #t)
      ((pred (car x)) (list-of-same? pred (cdr x)))
      (else #f))))
      
      
      
      