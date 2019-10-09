#lang racket

(require "env.rkt")
(define atom? (lambda (x)
                (not (list? x))))

(define parse
  (lambda (input)
    (cond
      [(not (pair? input)) (expression input)]
      [(eq? (car input) 'define) (new-define-exp (cadr input) (expression (caddr input)))]
      [else (expression input)])))

(define new-define-exp
  (lambda (sym val)
    (list 'define sym val)))

(define expression
  (lambda (input)
    (cond
      [(number? input) (new-lit-exp input)]
      [(atom? input) (new-var-ref input)]
      [else (error 'expression "Invalid syntax ~s" input)])))

(define new-lit-exp
  (lambda (input)
    (list 'number input)))

(define new-var-ref
  (lambda (sym)
     (list 'var-ref sym)))

(define Symbol (lambda (v)
                 (cadr  v)))

(define var-ref? (lambda (x)
                  (cond
                    [(atom? x) #f]
                    [else (eq? 'var-ref (car x))])))

(define define-exp? (lambda (x)
               (cond
                 [(atom? x) #f]
                 [else (eq? 'define (car x))])))

(define define-exp-sym
  (lambda (exp)
    (new-var-ref (cadr exp))))

(define define-exp-exp
  (lambda (exp)
    (caddr exp)))

;(define init-env
 ; (lambda (input)
  ;  (extended-env '(number) input the-empty-env)))

(define lit-exp?
  (lambda (x)
    (cond
      [(atom? x) #f]
      [else (eq? 'number (car x))])))

(define LitValue
  (lambda (tree) (cadr tree)))

(provide parse expression new-var-ref var-ref? Symbol lit-exp? LitValue define-exp? define-exp-sym define-exp-exp)