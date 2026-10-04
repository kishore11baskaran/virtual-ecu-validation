from simulation.engine import EngineModel


def test_engine_initial_state():
    engine = EngineModel()

    assert engine.rpm == 0
    assert engine.temperature == 25.0
    assert engine.load == 0.0


def test_engine_start():
    engine = EngineModel()

    engine.start()

    assert engine.rpm == 800
    assert engine.load == 10.0


def test_engine_stops():
    engine = EngineModel()

    engine.start()
    engine.stop()

    assert engine.rpm == 0
    assert engine.load == 0.0

    def test_engine_responds_to_throttle():
     engine = EngineModel()

    engine.start()

    initial_rpm = engine.rpm

    engine.update(1.0)

    assert engine.rpm > initial_rpm


def test_engine_rejects_invalid_throttle():
    engine = EngineModel()

    engine.start()

    try:
        engine.update(2.0)
        assert False
    except ValueError:
        assert True


