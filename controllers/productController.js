const Product = require('../model/Product');

const createProduct = async (req , res) =>{
    try{
         const {name, price, description, stock} = req.body;
         const product = new Product({name, price, description, stock});
         await product.save();
         res.status(201).json(product);
    }catch(err){
        res.status(500).json({message: err.message});
    }
}

const getProducts = async (req , res) =>{
    try{
        const products = await Product.find()
        res.status(200).json(Product)
    }catch(err) {
        res.status(500).json({message: err.message});
    }
}

module.exports = {
    createProduct,
    getProducts
}