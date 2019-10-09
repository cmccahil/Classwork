#lang racket

(define top
  (lambda (x)
    x))

(define atom? (lambda (x) (not (pair? x))))

(define rember-k
  (lambda (a lat k)
    (cond
      [(null? lat) (k null)]
      [(eq? a (car lat)) (k (cdr lat))]
      [else (rember-k a (cdr lat) (lambda (y) (k (cons (car lat) y))))])))

(define index-k
  (lambda (a lat k)
    (cond
      [(null? lat) -1]
      [(eq? a (car lat)) (k 0)]
      [else (index-k a (cdr lat) (lambda (x) (k (+ x 1))))])))


(define max-k
  (lambda (L k)
    (cond
      [(null? L) (k 0)]
      [(atom? (car L)) (if (> (car L) (max-k (cdr L) k))
                           (k (car L))
                           (max-k (cdr L) k))]
      [else (max-k (car L) (lambda (x)
                             (max-k (cdr L) (lambda (y)
                                              (k (if (> x y) x y))))))])))
                 
(define replace-k
  (lambda (old new L k)
    (cond
      [(null? L) (k null)]
      [(atom? (car L))
       (if (eq? old (car L))
           (replace-k old new (cdr L) (lambda (y) (k (cons new y))))
           (replace-k old new (cdr L) (lambda (y) (k (cons (car L) y)))))]
      [else (replace-k old new (car L) (lambda (x)
                                         (replace-k old new (cdr L) (lambda (y)
                                                                      (k (cons x y))))))])))

(define pairone-k
  (lambda (a L k)
    (if (null? L)
        (k null)
        (pairone-k a (cdr L) (lambda (x)
                               (k (cons (list a (car L)) x)))))))

(define pairall-k
  (lambda (L1 L2 k)
    (if (null? L1)
        (k null)
        (pairall-k (cdr L1) L2 (lambda (x) (append (pairone-k (car L1) L2 k) x))))))

      
