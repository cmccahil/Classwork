#lang racket

(require "env.rkt")
(define atom? (lambda (x)
                (not (list? x))))

(define parse
  (lambda (input)
    (cond
      [(not (pair? input)) (expression input)]
      [(eq? (car input) 'define) (new-define-exp (cadr input) (expression (caddr input)))]
      [(eq? (car input) 'if) (new-if-exp (cadr input) (caddr input) (cadddr input))]
      [(list? input) (new-app-exp (car input) (cdr input))]
      [else (expression input)])))

(define new-if-exp
  (lambda (conditional true-statement false-statement)
    (list 'if-exp (parse conditional) (parse true-statement) (parse false-statement))))

(define new-app-exp
  (lambda (proc values)
    (list 'app-exp (parse proc) (map parse values))))

(define app-exp?
  (lambda (exp)
    (cond
      [(atom? exp) #f]
      [else (eq? (car exp) 'app-exp)])))

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

(define apply-primitive-op (lambda (op arg-values)
                             (cond
                               [(eq? op '+) (+ (car arg-values) (cadr arg-values))]
                               [(eq? op '-) (- (car arg-values) (cadr arg-values))]
                               [(eq? op '*) (* (car arg-values) (cadr arg-values))]
                               [(eq? op '/) (/ (car arg-values) (cadr arg-values))]
                               [(eq? op 'add1) (add1 (car arg-values))]
                               [(eq? op 'sub1) (sub1 (car arg-values))]
                               [(eq? op 'minus) (* -1 (car arg-values))]
                               [(eq? op 'list) arg-values]
                               [(eq? op 'build) (cons (car arg-values) (cadr arg-values))]
                               [(eq? op 'first) (car arg-values)]
                               [(eq? op 'rest) (cdr arg-values)]
                               [(eq? op 'empty?) (null? arg-values)]
                               [(eq? op 'equals?) (if (eqv? (car arg-values) (cadr arg-values)) 'True 'False)]
                               [(eq? op 'lt?) (if (< (car arg-values) (cadr arg-values)) 'True 'False)]
                               [(eq? op 'gt?) (if (> (car arg-values) (cadr arg-values)) 'True 'False)])))

(define prim-proc-op (lambda (p) (cadr p)))

(define prim-proc? (lambda(x)
                     (cond
                       [(atom? x) #f]
                       [else (eq? (car x) 'prim-proc)])))

                        

(define apply-proc (lambda (p arg-values)
                     (cond
                       [(prim-proc? p) (apply-primitive-op (prim-proc-op p) arg-values)]
                       [else (error 'apply-proc "Bad procedure: ~s" p)])))

(define if-exp? (lambda (x)
                  (cond
                    [(atom? x) #f]
                    [else (eq? (car x) 'if-exp)])))


(provide parse expression new-var-ref var-ref? Symbol lit-exp? LitValue define-exp? define-exp-sym define-exp-exp new-app-exp
         apply-primitive-op prim-proc-op prim-proc? apply-proc app-exp? new-if-exp if-exp?)