class Environment:          #환경모듈은 투자할 차트 데이터 관리하는 작은 모듈
    PRICE_IDX = 4  # 종가의 위치

    def __init__(self, chart_data=None):
        self.chart_data = chart_data   #chart_data : 주식 종목의 차트데이터(2차원 배열)
        self.observation = None        #observation : 현재 관측치
        self.idx = -1                  #idx : 차트 데이터에서의 현재 위치

    def reset(self):            #reset() : observation,idx 초기화
        self.observation = None
        self.idx = -1

    def observe(self):          #observe() : idx를 다음 위치(하루 앞)으로 이동하고 observation을 업데이트.
        if len(self.chart_data) > self.idx + 1:
            self.idx += 1
            self.observation = self.chart_data.iloc[self.idx]
            return self.observation
        return None

    def get_price(self):        #get_price() : 현재 observation에서 종가 획득.
        if self.observation is not None:    #observation은 하나의 행이고 인덱스4인 observation[4]가 종가
            return self.observation[self.PRICE_IDX]
        return None

    def set_chart_data(self, chart_data):
        self.chart_data = chart_data
