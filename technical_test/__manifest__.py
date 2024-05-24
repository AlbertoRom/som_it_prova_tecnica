{
    "name": "Technical test",
    "summary": "Technical test module",
    "version": "16.0",
    "category": "Product",
    "author": "Alberto Romero Cabezas",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "product"
    ],
    "data": [
        'security/ir.model.access.csv',
        'data/product_categories.xml',
        'data/products.xml',
        'views/product_category.xml',
        'views/consumption.xml',
    ],
    "demo": [
        'demo/consumption.xml'
    ]
}
