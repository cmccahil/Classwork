#lang racket
(define atom?
  (lambda(y)
    (cond
      [(null? y)#f]
      [(list? y)#f]
      [else #t])))
    
  
