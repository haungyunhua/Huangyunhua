CXXFLAGS=-O3 -pipe -W -Wall -fPIC -D_LINUX_ -D_USE_MC_PACK_ -std=gnu++11
CFLAGS=$(CXXFLAGS)

INCPATH= -I${PADDLE_ROOT}/ \
		 -I${PADDLE_ROOT}/third_party/install/gflags/include \
		 -I${PADDLE_ROOT}/third_party/install/boost_1_41_0 \
		 -I${PADDLE_ROOT}/third_party/install/glog/include \
		 -I${PADDLE_ROOT}/third_party/install/protobuf/include \
		 -I${PADDLE_ROOT}/third_party/install/lac/output/include \
		 -I${PADDLE_ROOT}/third_party/eigen3 \
		 -I${PADDLE_ROOT}/third_party/install/mklml/include/

DEP_LDFLAGS= -L${PADDLE_ROOT}/paddle/fluid/inference \
			 -L${PADDLE_ROOT}/third_party/install/gflags/lib \
			 -L${PADDLE_ROOT}/third_party/install/lac/output/lib \
			 -L${PADDLE_ROOT}/third_party/install/mklml/lib/ -lmklml_intel \
			 -L${PADDLE_ROOT}/third_party/install/mklml/lib/ -liomp5 \

DEP_LDLIBS= -llac -lpcre -lpthread -lcrypto -lm -lgflags -lpaddle_fluid -lrt -ldl 

CXX=${GCC_BIN}
CC=$(CXX) $(CFLAGS)

PATTERN=./*.cpp
TESTFILES=$(wildcard $(PATTERN))
EXE=senti_cls_dnn

SRC_OBJ=main.o senti_cls_dnn.o wordseg.o\

all : $(EXE) output

$(EXE) : % : $(SRC_OBJ)
	$(CXX) $^ -o $@ $(CXXFLAGS) $(INCPATH) $(DEP_LDFLAGS) $(DEP_LDLIBS)

%.o : ./%.cpp
	$(CXX) $^ -c -o $@ $(CXXFLAGS) $(INCPATH)

output:
	if [ ! -d bin/ ]; then mkdir bin/; fi
	mv $(EXE) bin/
	rm -f *.o

.PHONY: list clean

	@echo $(EXE)

clean:
	rm -f *.o
	rm -Rf bin/

