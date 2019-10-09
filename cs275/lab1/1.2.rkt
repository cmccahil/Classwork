#lang racket
(define atom?
  (lambda(y)
    (cond
      [(null? y)#f]
      [(list? y)#f]
      [else #t])))

(define lat?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((atom? (car l)) (lat? (cdr l)))
      (else #f))))