import streamlit as st


def page():
    st.subheader("프로젝트 효과")
    st.write("프로젝트의 영향력은 다양한 개인들에게 실제 상황에서 적용 가능한 인공지능 기술을 제공하는 것에 있습니다. 이를 통해 다양한 분야에서 혁신과 효율성을 증진시키고, 이론적인 인공지능 지식과 실용적 적용 기술 간의 격차를 해소합니다. 이 프로젝트는 참가자들에게 인공지능이 특정 상황에서 어떻게 변혁적인 도구가 될 수 있는지에 대한 깊은 이해를 제공하며, 목표는 단순히 인공지능 기술을 배우는 것이 아니라, 이를 실제로 적용하여 다양한 분야에서 실질적이고 측정 가능한 개선을 창출하는 것입니다.")

    st.subheader("프로젝트 샘플 소개")
    tab1, tab2, tab3 = st.tabs(["초심자", "데이터 보유자", "개발자"])
    with tab1:
        st.write("사업체 대표, 특정업무 담당자, 스마트팜 운영 농민 들을 대상으로 한 프로젝트 결과물 제출물 샘플사항 입니다")
        st.divider()
        st.subheader("📝사업체 대표 프로젝트 결과물 샘플")
        st.write("ㆍ개요: 고객 서비스 효율성 향상을 위한 인공지능 도입")
        st.write("ㆍ기존방식: 수동 고객 문의 처리로 인해 지연된 응답 시간과 높은 오류율")
        st.write("ㆍ새로운 AI 접근: 예측형 인공지능 모델을 활용하여 고객 문의 자동 분류 및 우선 순위 설정")
        st.write("ㆍ성과: 응답 시간 단축, 고객 만족도 향상, 처리량 증가")
        st.write("ㆍ비교 분석: AI 도입 전후 고객 서비스 관련 지표 개선")

        st.subheader("📝데이터 보유 사업체 담당자 프로젝트 결과물 샘플")
        st.write("ㆍ개요: 판매 예측을 통한 재고 관리 최적화")
        st.write("ㆍ기존방식: 수동 분석 기반의 부정확한 재고 관리")
        st.write("ㆍ새로운 AI 접근: 예측형 인공지능 모델을 이용한 판매 데이터 분석 및 재고 최적화")
        st.write("ㆍ성과: 판매 예측 정확도 향상, 재고 비용 감소, 판매 손실 최소화")
        st.write("ㆍ비교 분석: AI 도입 전후 재고 관리 및 판매 예측 지표 개선")

        st.subheader("📝스마트팜 운영 농민 프로젝트 결과물 샘플")
        st.write("ㆍ개요: 작물 생산량 예측을 통한 수확 관리 개선")
        st.write("ㆍ기존방식: 경험에 의존한 비효율적인 작물 관리")
        st.write("ㆍ새로운 AI 접근: 예측형 AI를 활용한 작물 생산량 및 수확 시기 예측")
        st.write("ㆍ성과: 생산량 예측 정확도 향상, 수확량 증가, 낭비 감소")
        st.write("ㆍ비교 분석: AI 도입 전후 작물 관리 및 수확 효율성 개선")

    with tab2:
        st.write("데이터를 보유하였지만, 분석 및 인공지능 모델을 적용해서 실험 및 학술적 분석, 또는 업무를 개선시키는 사용자 그룹들의 프로젝트 주제와 결과물 샘플")
        st.subheader("📝학교 연구실을 위한 프로젝트 결과물 샘플")
        st.divider()
        st.write("프로젝트 주제: ")
        st.write("🚩실험 데이터를 활용한 과학 연구 분석")
        st.write("ㆍ개요: 실험 데이터 분석을 통한 연구 결과의 정확성 향상")
        st.write("ㆍ기존방식: 전통적인 통계 방법을 사용한 기본 데이터 분석")
        st.write("ㆍ새로운 AI 접근: 예측형 인공지능 모델을 사용하여 실험 데이터의 복잡한 패턴 분석 및 결과 예측")
        st.write("ㆍ성과: 분석의 정확도와 신뢰성 증가, 연구 결과의 품질 향상")
        st.write("ㆍ적용 인공지능 모델: 예측형 모델 사용, 실험 데이터의 복잡한 패턴 인식 및 예측")
        st.write("ㆍ비교 분석: AI 도입 전후의 데이터 분석 효율성과 연구 결과의 질적 개선")

        st.write("프로젝트 주제: ")
        st.write("🚩설문조사 데이터를 통한 사회과학 연구")
        st.write("ㆍ개요: 설문조사 데이터 분석을 통한 심층적인 사회 연구 수행")
        st.write("ㆍ기존방식: 수동 데이터 분석 및 제한된 통찰력")
        st.write("ㆍ새로운 AI 접근: 예측형 인공지능 모델을 활용하여 설문 데이터에서 숨겨진 패턴 및 인사이트 발견")
        st.write("ㆍ성과: 연구의 심층성과 정확성 향상, 보다 광범위한 데이터 분석 가능")
        st.write("ㆍ적용 인공지능 모델: 예측형 모델 사용, 설문 데이터에서 숨겨진 트렌드와 패턴 예측")
        st.write("ㆍ비교 분석: AI 도입 전후의 연구 결과의 심층성 및 정확성 개선")

    with tab3:
        st.write("개발자 사용자그룹을 대상으로 인공지능 모델을 만들거나, 생성형 인공지능을 활용하여 코드를 작성하는 방법을 적용하여 효율성을 높이는 프로젝트 결과물 샘플")
        st.divider()
        st.write("프로젝트 주제: ")
        st.subheader("📝ChatGPT를 활용한 코드 개선 및 최적화")
        st.write("ㆍ개요: ChatGPT를 이용하여 프로그래밍 과정에서의 효율성 및 코드 품질 향상")
        st.write("ㆍ기존방식: 전통적인 코드 작성 및 디버깅 방법")
        st.write("ㆍ새로운 AI 접근: ChatGPT를 활용한 코드 작성 지원 및 복잡한 문제 해결")
        st.write("ㆍ성과: 개발 시간 단축, 코드 품질 향상, 문제 해결 능력 증대")
        st.write("ㆍ적용 인공지능 모델: ChatGPT를 이용한 코드 작성 및 최적화")
        st.write("ㆍ비교 분석: AI 도입 전후의 개발 프로세스 효율성 및 코드 품질 개선")

        st.write("프로젝트 주제: ")
        st.subheader("📝Wonder Lab을 통한 인공지능 모델 자동 생성 및 웹앱 적용")
        st.write("ㆍ개요: 자동화된 인공지능 모델 생성 및 웹앱에 통합하여 사용자 경험 개선")
        st.write("ㆍ기존방식: 수동 인공지능 모델 개발 및 통합")
        st.write("ㆍ새로운 AI 접근: Wonder Lab 플랫폼을 이용한 AI 모델 자동 생성 및 웹앱에 적용")
        st.write("ㆍ성과: 개발 및 통합 시간 단축, 사용자 경험의 질적 향상")
        st.write("ㆍ적용 인공지능 모델: 자동 생성된 인공지능 모델을 이용한 웹앱 통합")
        st.write("ㆍ비교 분석: AI 도입 전후의 웹앱 개발 및 사용자 경험 개선")