#lang racket
(require "TreeDatatype.rkt")
                          
(define childSum
  (lambda (tree)
    (foldr (lambda (x y) (+ (cadr x) y))
            0
            (list-of-children tree))))

(define atom? (lambda (x)
                (not (list? x))))

(define numbersIn
  (lambda (L)
    (cond
      [(null? L) null]
      [(atom? L) (if (number? L) (list L) null)]
      [else (apply append (map numbersIn L))])))

(define allSum
  (lambda (tr)
    (+ (value tr) (foldr + 0 (numbersIn (list-of-children tr))))))

(define visitTree
  (lambda (f tr)
    (cond
      [(null? tr) null]
      [(number? tr) (f tr)]
      [(atom? tr) tr]
      [else (map(lambda(x)(visitTree f x))tr)])))

(define sizeof 
  (lambda (tr)
    (cond
      [(null? tr) 0]
      [(number? tr) 1]
      [(atom? tr) 0]
      [else (apply + (map sizeof tr))])))

(define height 
  (lambda (tr)
    (cond
      [(empty-tree? tr) -1]
      [(leaf? tr) 0]
      [else (+ 1 (apply max (map height (list-of-children tr))))])))

(define count
  (lambda (n tr)
    (letrec([h (lambda (x)
                 (cond
                   [(null? x) 0]
                   [(and (number? x) (= x n)) 1]
                   [(atom? x) 0]
                   [else (apply + (map h x))]))])
      (h tr))))


(define preorder
  (lambda (tr)
    (cond
      [(leaf? tr) (list (value tr))]
      [else (cons (value tr) (apply append (map preorder (list-of-children tr))))])))

(define postorder
  (lambda (tr)
    (cond
      [(leaf? tr) (list (value tr))]
      [else (append (apply append (map postorder (list-of-children tr))) (list (value tr)))])))
      
      

    