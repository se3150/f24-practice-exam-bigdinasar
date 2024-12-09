import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b




def describe_Battery():

    def get_capacity_returns_capacity():
        
        cb = Battery(100)
        assert cb.getCapacity() == 100

    def get_charge_returns_charge():
        
        pcb = Battery(100)
        pcb.drain(30)
        assert pcb.getCharge() == 70

    def describe_recharge():
        # your test cases here'
        
        def it_wont_charge_a_full_battery():
            cb = Battery(100)
            assert cb.recharge(10) == False

        def it_wont_accept_a_charge_greater_than_cap():
            cb = Battery(10)
            assert cb.recharge(110) == False

        def if_charge_would_exceed_cap_it_sets_charge_to_cap():
            cb = Battery(100)
            cb.drain(10)
            cb.recharge(100)
            assert cb.getCharge() == 100

        def it_notifies_recharge_called_once():
            
            mock_monitor = Mock()
            cb = Battery(100, external_monitor = mock_monitor)
        
            cb.drain(20)
            cb.recharge(100)

            mock_monitor.notify_recharge.assert_called_once_with(100)

        

        

    def describe_drain():
        # your test cases here
        todo


