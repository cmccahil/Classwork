#lang racket
(define current '())
(define buffer '())
(define helper
  (lambda (lat n)
    (cond
      [(< (last lat) n) (set! current (append current (list n)))]
      [(< (car lat) n) (set! buffer (append buffer (list (car lat)))) (helper (cdr lat) n)]
      [else (set! buffer (append buffer (list n))) (set! buffer (append buffer lat)) (set! current buffer) (set! buffer '())])))
      
  
(define sort
  (lambda (lat)
    (cond
      [(null? current) (set! current (list (car lat))) (sort lat)]
      [(= (length lat) 1) (set! buffer current) (set! current '()) buffer]
      [else (set! buffer '()) (helper current (cadr lat)) (sort (cdr lat)) ])))
      