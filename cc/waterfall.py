import csv

data_path = 'x.csv'


class Pot:
    def __init__(self, cat, lim, bal, pot, q):
        self.cat = cat  # Category: either 'call' or 'dist'
        self.lim = lim  # Limit: limited by investors' calls / dists
        self.bal = bal  # Balance: current pot balance (all portfolios)
        self.free_space = self.lim - self.bal  # Free space: how much space available in the pot for additional stuff
        self.pot = pot  # Pot: store information on which CFItem is inside the pot
        self.q = q  # Queue: store information on which CFItem is in the queue to be put in the pot

    def update_lim(self, extra_lim):
        self.lim += extra_lim
        self.free_space += extra_lim

    def update_bal(self, extra_bal):
        self.bal += extra_bal
        self.free_space = self.lim - self.bal

    def getPortfBal(self, portf):
        portf_bal = 0
        for item in self.pot:
            if item.portf == portf:
                portf_bal += item.amt_ip

        return portf_bal

    def process_q(self):
        # Check if there's free space in the pot
        if self.free_space > 0:
            # Check the queue for available items
            if len(self.q) > 0:
                item_q = self.q[0]

                # Check if this is the first time this item is put in this pot
                # so we can update the pot's pot, otherwise do nothing
                if len(self.pot) == 0 or self.pot[len(self.pot) - 1].tag != item_q.tag:
                    self.pot.append(item_q)

                # Update the pot's and the item's properties
                new_free_space = item_q.put_in_pot(self.free_space)
                self.update_bal(self.free_space - new_free_space)

                # Remove the item from the queue if necessary
                if item_q.amt_op == 0:
                    self.q.pop(0)

                # Recurse
                self.process_q()


class CFItem:
    def __init__(self, tag, cat, portf, lp, date, amt):
        self.tag = tag
        self.cat = cat
        self.portf = portf
        self.lp = lp
        self.date = date
        self.amt_org = amt  # Original amount
        self.amt_op = amt  # Out-of-pot amount
        self.amt_ip = 0  # In-pot amount

    def put_in_pot(self, free_space):
        rem_space = free_space
        if free_space >= self.amt_op:
            # Let's put everything in the pot!
            amt_to_put_in = self.amt_op
            self.amt_op -= amt_to_put_in
            self.amt_ip += amt_to_put_in
            rem_space -= amt_to_put_in
        else:
            # Not enough space in the pot...Let's put a bit in
            self.amt_op -= free_space
            self.amt_ip += free_space
            rem_space = 0

        return rem_space


def main():
    cf_list = []

    # Read & record initial data
    with open(data_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        iter_reader = iter(reader)
        next(iter_reader)

        tag = 0

        for row in iter_reader:
            row_data = row[0].split(';')

            cat = row_data[0].lower()
            portf = row_data[1].lower()
            lp = row_data[2].lower()
            date = row_data[3]
            if row_data[4] == ' -   ':
                amt = 0
            elif cat == 'investor call' or cat == 'portfolio call' or cat == 'expense':
                amt = -float(row_data[4])
            else:
                amt = float(row_data[4])

            cf_item = CFItem(tag, cat, portf, lp, date, amt)
            cf_list.append(cf_item)

            tag += 1

        print('Read & recorded a total of {} cashflow transactions.'.format(len(cf_list)))

    # Initialise pots
    pot_call = Pot('call', 0, 0, [], [])
    pot_dist = Pot('dist', 0, 0, [], [])

    # Loop through each cf item
    for cf in cf_list:
        # Initial classifications / pot updates
        if cf.cat == 'investor call':
            pot_call.update_lim(cf.amt_org)
        elif cf.cat == 'investor dist.':
            pot_dist.update_lim(cf.amt_org)
        elif cf.cat == 'portfolio call' or cf.cat == 'expense':
            pot_call.q.append(cf)
        elif cf.cat == 'portfolio dist.' or cf.cat == 'income':
            pot_dist.q.append(cf)

        # Process available queues
        pot_call.process_q()
        pot_dist.process_q()

    # Print final results
    print('\n'
          'Pot call ***')
    print('Limit: {:,}\n'
          'Balance: {:,}\n'
          'Remaining space: {:,}\n'
          'Total items in pot: {:,}\n'
          'Total A balance in pot: {:,}\n'
          'Total B balance in pot: {:,}\n'
          'Total CD Gen 8 Asia balance in pot: {:,}\n'
          .format(pot_call.lim, pot_call.bal, pot_call.free_space, len(pot_call.pot),
                  pot_call.getPortfBal('a'), pot_call.getPortfBal('b'), pot_call.getPortfBal('a (gen 8 asian)')))

    print('\n'
          'Pot dist ***')
    print('Limit: {:,}\n'
          'Balance: {:,}\n'
          'Remaining space: {:,}\n'
          'Total items in pot: {:,}\n'
          'Total A balance in pot: {:,}\n'
          'Total B balance in pot: {:,}\n'
          'Total CD Gen 8 Asia balance in pot: {:,}\n'
          .format(pot_dist.lim, pot_dist.bal, pot_dist.free_space, len(pot_dist.pot),
                  pot_dist.getPortfBal('a'), pot_dist.getPortfBal('b'), pot_dist.getPortfBal('a (gen 8 asian)')))


main()
