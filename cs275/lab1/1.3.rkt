#lang racket
(define atom?
  (lambda(y)
    (cond
      [(null? y)#f]
      [(list? y)#f]
      [else #t])))

(define not-lat?
  (lambda (l)
    (cond
      ((null? l) #f)
      ((atom? (car l)) (not-lat? (cdr l)))
      (else #t))))
    