(set-logic QF_NRA)
(declare-fun a () Int [0, 1])
;; (declare-fun c () Int [-10, 10])
(assert (= 0 (^ 0 a)))
;; (assert (= c 5))
(check-sat)
(exit)
