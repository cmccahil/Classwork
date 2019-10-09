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
      [(eq? (car input) 'let) (new-let-exp input)]
      [(eq? (car input) 'lambda) (new-lambda-exp input)]
      [(eq? (car input) 'set!) (new-assign-exp (cadr input) (caddr input))]
      [(eq? (car input) 'begin) (new-begin-exp input)]
      [(eq? (car input) 'letrec) (parse (new-letrec-exp (binding-syms (BindingList input)) (binding-vals (BindingList input)) (binding-rand-syms (BindingList input)) (caddr input)))]
      [(list? input) (new-app-exp (car input) (cdr input))]
      [else (expression input)])))

(define begin-exp?
  (lambda (x)
    (cond
      [(atom? x) #f]
      [else (eq? (car x) 'begin-exp)])))

(define new-begin-exp
  (lambda (exps)
    (cond
      [(null? exps) null]
      [(eq? 'begin (car exps)) (cons 'begin-exp (new-begin-exp (cdr exps)))]
      [else (cons(parse (car exps)) (new-begin-exp (cdr exps)))])))

(define new-assign-exp
  (lambda (sym val)
    (list 'assign-exp sym (parse val))))

(define assign-exp?
  (lambda (x)
    (cond
      [(atom? x) #f]
      [else (eq? (car x) 'assign-exp)])))

(define closure
  (lambda (params body env)
    (list 'closure params body env)))

(define new-lambda-exp
  (lambda (exp)
    (list 'lambda-exp (cadr exp) (parse (caddr exp)))))
    
(define lambda-exp?
  (lambda (x)
    (cond
      [(atom? x) #f]
      [else (eq? (car x) 'lambda-exp)])))

(define BindingList
  (lambda (exp)
    (cadr exp)))

(define binding-syms
  (lambda (binding-list)
    (map car binding-list)))

(define binding-vals
  (lambda (binding-list)
    (map cadr binding-list)))

(define binding-rand-syms
  (lambda (binding-list)
    (cond
      [(null? binding-list) null]
      [else (cons (gensym) (binding-rand-syms (cdr binding-list)))])))

(define new-letrec-exp
  (lambda (syms vals rand-syms body)
    (list 'let (zero-bindings syms) (list 'let (rand-bindings rand-syms vals) (set-expressions syms rand-syms (car syms) body)))))

(define set-expressions
  (lambda (syms rand-syms start-variable body)
    (cond
      [(null? syms) (list body)]
      [(eq? start-variable (car syms)) (cons 'begin (set-expressions syms rand-syms -1 body))]
      [else (cons (list 'set! (car syms) (car rand-syms)) (set-expressions (cdr syms) (cdr rand-syms) start-variable body))])))

(define rand-bindings
  (lambda (syms vals)
    (cond
      [(null? syms) null]
      [else (cons (list (car syms) (car vals)) (rand-bindings (cdr syms) (cdr vals)))])))

(define zero-bindings
  (lambda (exp)
    (cond
      [(null? exp) null]
      [else (cons (list (car exp) 0) (zero-bindings (cdr exp)))])))
    

(define new-let-exp
  (lambda (exp)
    (list 'let-exp (map (lambda(x) (car x)) (cadr exp)) (map parse (map (lambda(x) (cadr x)) (cadr exp))) (parse (caddr exp)))))

(define let-exp?
  (lambda (exp)
    (cond
      [(atom? exp) #f]
      [else (eq? (car exp) 'let-exp)])))

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

                        



(define if-exp? (lambda (x)
                  (cond
                    [(atom? x) #f]
                    [else (eq? (car x) 'if-exp)])))

(define closure? (lambda (x)
                   (cond
                     [(atom? x) #f]
                     [else (eq? (car x) 'closure)])))


(provide parse expression new-var-ref var-ref? Symbol lit-exp? LitValue define-exp? define-exp-sym define-exp-exp new-app-exp
         apply-primitive-op prim-proc-op prim-proc? app-exp? new-if-exp if-exp? let-exp? new-lambda-exp closure closure?
         lambda-exp? assign-exp? new-assign-exp begin-exp? new-begin-exp)