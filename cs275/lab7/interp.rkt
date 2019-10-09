#lang racket

(require "env.rkt")
(require "parse.rkt")

(define eval-exp 
  (lambda (exp env) 
    (cond
      [(lit-exp? exp) (LitValue exp)]
      [(var-ref? exp) (unbox (lookup-env env (Symbol exp)))]
      [(define-exp? exp) (let ([sym (define-exp-sym exp)]
                               [val (eval-exp (define-exp-exp exp) env)])
                           (do-define sym val))]
      [(app-exp? exp) (apply-proc (eval-exp (cadr exp) env) (map (lambda (t)(eval-exp t env)) (caddr exp)))] ;evaluate the cadr (procedure) in the environment
      [(if-exp? exp) (if (eq? 'True (eval-exp (cadr exp) env)) (eval-exp (caddr exp) env) (eval-exp (cadddr exp) env))]
      [(let-exp? exp) (let ([syms (cadr exp)]
                            [vals (map (lambda (t) (eval-exp t env)) (caddr exp))]) (eval-exp (cadddr exp) (extended-env syms vals env)))]
      [(lambda-exp? exp) (closure (cadr exp) (caddr exp) env)]
      [(assign-exp? exp) (set-box! (lookup-env env (cadr exp)) (eval-exp (caddr exp) env))]
      [(begin-exp? exp) (cond
                          [(null? (cdr (cdr exp))) (eval-exp (cadr exp) env)]
                          [else (eval-exp (cadr exp) env) (eval-exp (cons 'begin-exp (cdr (cdr exp))) env)])]
      [else (error 'eval-exp  "Invalid symbol: ~s" exp)])))

(define apply-proc (lambda (p arg-values)
                     (cond
                       [(prim-proc? p) (apply-primitive-op (prim-proc-op p) arg-values)]
                       [(closure? p) (eval-exp (caddr p) (extended-env (cadr p) arg-values (cadddr p)))]
                       [else (error 'apply-proc "Bad procedure: ~s" p)])))

;[else (lookup-env env exp)])))
;What is a valid input and output supposed to look like?
;map eval-exp onto list of arguments

(provide eval-exp)