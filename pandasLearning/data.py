
# data_df
data_df = ['{"foreign_min":1,"foreign_max":2,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":4,"duration_max":72,"duration_q1":12.0,"duration_median":18.0,"duration_q3":24.0,"checking_min":1,"checking_max":4,"checking_q1":2.0,"checking_median":3.0,"checking_q3":4.0,"purpose":"3"}',
 '{"foreign_min":1,"foreign_max":1,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":6,"duration_max":24,"duration_q1":10.0,"duration_median":12.0,"duration_q3":12.0,"checking_min":1,"checking_max":4,"checking_q1":2.0,"checking_median":2.0,"checking_q3":4.0,"purpose":"8"}',
 '{"foreign_min":1,"foreign_max":2,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":4,"duration_max":60,"duration_q1":11.25,"duration_median":15.0,"duration_q3":24.0,"checking_min":1,"checking_max":4,"checking_q1":1.0,"checking_median":2.0,"checking_q3":4.0,"purpose":"0"}',
 '{"foreign_min":1,"foreign_max":2,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":6,"duration_max":42,"duration_q1":12.0,"duration_median":16.5,"duration_q3":24.0,"checking_min":1,"checking_max":4,"checking_q1":2.0,"checking_median":2.0,"checking_q3":4.0,"purpose":"5"}',
 '{"foreign_min":1,"foreign_max":1,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":6,"duration_max":60,"duration_q1":12.0,"duration_median":15.0,"duration_q3":36.0,"checking_min":1,"checking_max":4,"checking_q1":1.25,"checking_median":2.0,"checking_q3":4.0,"purpose":"6"}',
 '{"foreign_min":1,"foreign_max":2,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":8,"duration_max":60,"duration_q1":24.0,"duration_median":24.0,"duration_q3":48.0,"checking_min":1,"checking_max":4,"checking_q1":1.0,"checking_median":2.0,"checking_q3":2.0,"purpose":"X"}',
 '{"foreign_min":1,"foreign_max":2,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":5,"duration_max":60,"duration_q1":18.0,"duration_median":24.0,"duration_q3":36.0,"checking_min":1,"checking_max":4,"checking_q1":2.0,"checking_median":2.0,"checking_q3":4.0,"purpose":"9"}',
 '{"foreign_min":1,"foreign_max":2,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":6,"duration_max":54,"duration_q1":18.0,"duration_median":24.0,"duration_q3":36.0,"checking_min":1,"checking_max":4,"checking_q1":1.5,"checking_median":4.0,"checking_q3":4.0,"purpose":"1"}',
 '{"foreign_min":1,"foreign_max":1,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":6,"duration_max":48,"duration_q1":9.75,"duration_median":13.5,"duration_q3":15.75,"checking_min":1,"checking_max":4,"checking_q1":1.0,"checking_median":2.0,"checking_q3":4.0,"purpose":"4"}',
 '{"foreign_min":1,"foreign_max":2,"foreign_q1":1.0,"foreign_median":1.0,"foreign_q3":1.0,"duration_min":4,"duration_max":48,"duration_q1":12.0,"duration_median":18.0,"duration_q3":24.0,"checking_min":1,"checking_max":4,"checking_q1":1.0,"checking_median":2.0,"checking_q3":4.0,"purpose":"2"}']

data_rdd = [{'checking_max': 4,
  'checking_median': 3.0,
  'checking_min': 1,
  'checking_q1': 2.0,
  'checking_q3': 4.0,
  'duration_max': 72,
  'duration_median': 18.0,
  'duration_min': 4,
  'duration_q1': 12.0,
  'duration_q3': 24.0,
  'foreign_max': 2,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '3'},
 {'checking_max': 4,
  'checking_median': 2.0,
  'checking_min': 1,
  'checking_q1': 2.0,
  'checking_q3': 4.0,
  'duration_max': 24,
  'duration_median': 12.0,
  'duration_min': 6,
  'duration_q1': 10.0,
  'duration_q3': 12.0,
  'foreign_max': 1,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '8'},
 {'checking_max': 4,
  'checking_median': 2.0,
  'checking_min': 1,
  'checking_q1': 1.0,
  'checking_q3': 4.0,
  'duration_max': 60,
  'duration_median': 15.0,
  'duration_min': 4,
  'duration_q1': 11.25,
  'duration_q3': 24.0,
  'foreign_max': 2,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '0'},
 {'checking_max': 4,
  'checking_median': 2.0,
  'checking_min': 1,
  'checking_q1': 2.0,
  'checking_q3': 4.0,
  'duration_max': 42,
  'duration_median': 16.5,
  'duration_min': 6,
  'duration_q1': 12.0,
  'duration_q3': 24.0,
  'foreign_max': 2,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '5'},
 {'checking_max': 4,
  'checking_median': 2.0,
  'checking_min': 1,
  'checking_q1': 1.25,
  'checking_q3': 4.0,
  'duration_max': 60,
  'duration_median': 15.0,
  'duration_min': 6,
  'duration_q1': 12.0,
  'duration_q3': 36.0,
  'foreign_max': 1,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '6'},
 {'checking_max': 4,
  'checking_median': 2.0,
  'checking_min': 1,
  'checking_q1': 1.0,
  'checking_q3': 2.0,
  'duration_max': 60,
  'duration_median': 24.0,
  'duration_min': 8,
  'duration_q1': 24.0,
  'duration_q3': 48.0,
  'foreign_max': 2,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': 'X'},
 {'checking_max': 4,
  'checking_median': 2.0,
  'checking_min': 1,
  'checking_q1': 2.0,
  'checking_q3': 4.0,
  'duration_max': 60,
  'duration_median': 24.0,
  'duration_min': 5,
  'duration_q1': 18.0,
  'duration_q3': 36.0,
  'foreign_max': 2,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '9'},
 {'checking_max': 4,
  'checking_median': 4.0,
  'checking_min': 1,
  'checking_q1': 1.5,
  'checking_q3': 4.0,
  'duration_max': 54,
  'duration_median': 24.0,
  'duration_min': 6,
  'duration_q1': 18.0,
  'duration_q3': 36.0,
  'foreign_max': 2,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '1'},
 {'checking_max': 4,
  'checking_median': 2.0,
  'checking_min': 1,
  'checking_q1': 1.0,
  'checking_q3': 4.0,
  'duration_max': 48,
  'duration_median': 13.5,
  'duration_min': 6,
  'duration_q1': 9.75,
  'duration_q3': 15.75,
  'foreign_max': 1,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '4'},
 {'checking_max': 4,
  'checking_median': 2.0,
  'checking_min': 1,
  'checking_q1': 1.0,
  'checking_q3': 4.0,
  'duration_max': 48,
  'duration_median': 18.0,
  'duration_min': 4,
  'duration_q1': 12.0,
  'duration_q3': 24.0,
  'foreign_max': 2,
  'foreign_median': 1.0,
  'foreign_min': 1,
  'foreign_q1': 1.0,
  'foreign_q3': 1.0,
  'purpose': '2'}]



# result_rdd
result_rdd = [[{'foreign': (1, 2, 1.0, 1.0, 1.0, '3')},
  {'duration': (4, 72, 12.0, 18.0, 24.0, '3')},
  {'checking': (1, 4, 2.0, 3.0, 4.0, '3')}],
 [{'foreign': (1, 1, 1.0, 1.0, 1.0, '8')},
  {'duration': (6, 24, 10.0, 12.0, 12.0, '8')},
  {'checking': (1, 4, 2.0, 2.0, 4.0, '8')}],
 [{'foreign': (1, 2, 1.0, 1.0, 1.0, '0')},
  {'duration': (4, 60, 11.25, 15.0, 24.0, '0')},
  {'checking': (1, 4, 1.0, 2.0, 4.0, '0')}],
 [{'foreign': (1, 2, 1.0, 1.0, 1.0, '5')},
  {'duration': (6, 42, 12.0, 16.5, 24.0, '5')},
  {'checking': (1, 4, 2.0, 2.0, 4.0, '5')}],
 [{'foreign': (1, 1, 1.0, 1.0, 1.0, '6')},
  {'duration': (6, 60, 12.0, 15.0, 36.0, '6')},
  {'checking': (1, 4, 1.25, 2.0, 4.0, '6')}],
 [{'foreign': (1, 2, 1.0, 1.0, 1.0, 'X')},
  {'duration': (8, 60, 24.0, 24.0, 48.0, 'X')},
  {'checking': (1, 4, 1.0, 2.0, 2.0, 'X')}],
 [{'foreign': (1, 2, 1.0, 1.0, 1.0, '9')},
  {'duration': (5, 60, 18.0, 24.0, 36.0, '9')},
  {'checking': (1, 4, 2.0, 2.0, 4.0, '9')}],
 [{'foreign': (1, 2, 1.0, 1.0, 1.0, '1')},
  {'duration': (6, 54, 18.0, 24.0, 36.0, '1')},
  {'checking': (1, 4, 1.5, 4.0, 4.0, '1')}],
 [{'foreign': (1, 1, 1.0, 1.0, 1.0, '4')},
  {'duration': (6, 48, 9.75, 13.5, 15.75, '4')},
  {'checking': (1, 4, 1.0, 2.0, 4.0, '4')}],
 [{'foreign': (1, 2, 1.0, 1.0, 1.0, '2')},
  {'duration': (4, 48, 12.0, 18.0, 24.0, '2')},
  {'checking': (1, 4, 1.0, 2.0, 4.0, '2')}]]


# result_dict
result_dict = {'checking': [(1, 4, 2.0, 3.0, 4.0, '3'),
  (1, 4, 2.0, 2.0, 4.0, '8'),
  (1, 4, 1.0, 2.0, 4.0, '0'),
  (1, 4, 2.0, 2.0, 4.0, '5'),
  (1, 4, 1.25, 2.0, 4.0, '6'),
  (1, 4, 1.0, 2.0, 2.0, 'X'),
  (1, 4, 2.0, 2.0, 4.0, '9'),
  (1, 4, 1.5, 4.0, 4.0, '1'),
  (1, 4, 1.0, 2.0, 4.0, '4'),
  (1, 4, 1.0, 2.0, 4.0, '2')],
 'duration': [(4, 72, 12.0, 18.0, 24.0, '3'),
  (6, 24, 10.0, 12.0, 12.0, '8'),
  (4, 60, 11.25, 15.0, 24.0, '0'),
  (6, 42, 12.0, 16.5, 24.0, '5'),
  (6, 60, 12.0, 15.0, 36.0, '6'),
  (8, 60, 24.0, 24.0, 48.0, 'X'),
  (5, 60, 18.0, 24.0, 36.0, '9'),
  (6, 54, 18.0, 24.0, 36.0, '1'),
  (6, 48, 9.75, 13.5, 15.75, '4'),
  (4, 48, 12.0, 18.0, 24.0, '2')],
 'foreign': [(1, 2, 1.0, 1.0, 1.0, '3'),
  (1, 1, 1.0, 1.0, 1.0, '8'),
  (1, 2, 1.0, 1.0, 1.0, '0'),
  (1, 2, 1.0, 1.0, 1.0, '5'),
  (1, 1, 1.0, 1.0, 1.0, '6'),
  (1, 2, 1.0, 1.0, 1.0, 'X'),
  (1, 2, 1.0, 1.0, 1.0, '9'),
  (1, 2, 1.0, 1.0, 1.0, '1'),
  (1, 1, 1.0, 1.0, 1.0, '4'),
  (1, 2, 1.0, 1.0, 1.0, '2')]}