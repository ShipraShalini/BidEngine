from src.common.helpers.getrequest import read_request
from src.api.ES.helpers.bidhelper import get_bid
from django.contrib.auth.decorators import login_required



'''
no input, users should be logged in
'''
#view bids of an users
@login_required(login_url='http://localhost:8000/login_message/')
def view_bids(request):
    bidder, item_name = read_request(request)
    bid_dict= {}
    bid_list = get_bid(bidder=bidder)
    for bid in bid_list:
        print type(bid)
        bid_dict[bid.item] = int(bid.bid_amount)
    return "User: {0} \nBids: \n{1}".format(bidder, bid_dict)
