#lang racket

(define empty-env (lambda () (list 'empty-env)))
(define extended-env (lambda (syms vals old-env) (list 'extended-env syms vals old-env)))

(define empty-env? (lambda (x)
      (cond
            [(not (pair? x)) #f]
            [else (eq? (car x) 'empty-env)])))

(define extended-env? (lambda (x)
      (cond
            [(not (pair? x)) #f]
            [else (eq? (car x) 'extended-env)])))

(define environment? (lambda (x) (or (empty-env? x) (extended-env? x))))

(define syms (lambda (env)
     (cond
           [(extended-env? env) (cadr env)]
           [else (error 'syms "bad environment")])))


(define vals (lambda (env)
      (cond
            [(extended-env? env) (caddr env)]
            [else (error 'vals "bad environment")])))


(define old-env (lambda (env)
     (cond
           [(extended-env? env) (cadddr env)]
           [else (error 'old-env "bad environment")])))

(define the-empty-env (empty-env))

(define EnvA (extended-env '(x y) '(1 2) the-empty-env))
(define EnvB (extended-env '(x z) '(5 7) EnvA))

(define lookup-env
  (lambda (env sym)
    (if (empty-env? env) (error 'apply-env "No binding for ~s" sym)
        (let([symbols (syms env)]
             [values (vals env)])
            (h symbols values sym env)))))

(define h
  (lambda (symbols values sym env)
    (cond
      [(null? symbols) (lookup-env (old-env env) sym)]
      [(eq? (car symbols) sym) (car values)]
      [else (h (cdr symbols) (cdr values) sym env)])))

(define do-define
  (lambda (sym val)
    (set! init-env (extended-env sym val init-env))))

(define prim-ops '(+ - * / add1 sub1 minus list build first rest empty? nil equals? lt? gt?))

(define nil '())

(define new-prim-proc (lambda (op)
                        (list 'prim-proc op)))
;(define init-env (extended-env '(a b c) '(4 5 6)
 ;                            (extended-env '(a x y) '(1 2 3) empty-env)))
(define init-env1  (extended-env '(a b) '(5 6) (extended-env '(x) '(20) the-empty-env)))

(define init-env (extended-env prim-ops (map new-prim-proc prim-ops) init-env1))



(provide empty-env extended-env empty-env? extended-env? syms vals old-env the-empty-env EnvA EnvB lookup-env init-env do-define prim-ops nil)

