def push_pull(pred_tl, pred_br, mask_tl, mask_br):
  s1 = tf.gather_nd(pred_tl, mask_tl)
  s2 = tf.gather_nd(pred_br, mask_br)
  N = len(s1)
  push, pull = 0, 0
  m = []
  
  for a,b in zip(s1,s2):
    mean = (a+b)/2
    pull += tf.pow(a-mean, 2) + tf.pow(b-mean,2)
    m.append(mean)
  
  m = tf.convert_to_tensor(m)
  for i in range(len(m)):
    mask = np.ones(len(m))
    mask[i] = 0
    mask = tf.convert_to_tensor(mask)

    p = 1 - tf.math.abs(m - tf.gather_nd(m, [i]))
    p = p*mask
    push += tf.reduce_sum(p)

  pull = pull/N
  push = push/(N*(N-1))  

  return push, pull