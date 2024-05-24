from odoo.tests.common import TransactionCase


class TestConsumption(TransactionCase):

    def setUp(self):
        super(TestConsumption, self).setUp()
        self.consumption = self.env['consumption'].sudo().create({
            'product_id': 1,
            'date': '2019-01-01',
            'quantity': 100,
        })

    def test_create_consumption(self):
        self.assertEqual(self.consumption.product_id.id, 1)
        self.assertEqual(self.consumption.date, '2019-01-01')
        self.assertEqual(self.consumption.quantity, 100)

    def test_update_consumption(self):
        self.consumption.write({
            'product_id': 2,
            'date': '2019-02-01',
            'quantity': 200,
        })
        self.assertEqual(self.consumption.product_id.id, 2)
        self.assertEqual(self.consumption.date, '2019-02-01')
        self.assertEqual(self.consumption.quantity, 200)

    def test_delete_consumption(self):
        self.consumption.unlink()
        self.assertFalse(self.env['consumption'].search([
            ('id', '=', self.consumption.id)]))

    def test_read_consumption(self):
        read_consumption = self.env['consumption'].search([
            ('id', '=', self.consumption.id)])
        self.assertEqual(read_consumption.product_id.id, 1)
        self.assertEqual(read_consumption.date, '2019-01-01')
        self.assertEqual(read_consumption.quantity, 100)
