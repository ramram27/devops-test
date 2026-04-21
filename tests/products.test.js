import { describe, it, expect, vi, afterEach } from "vitest";
import controller from "../controllers/productController.js";
import Product from "../model/Product.js";
import { param } from "../routes/productRoutes.js";

const { createProduct ,getProducts } = controller;

afterEach(() => {
  vi.restoreAllMocks();
})

describe("createProduct", () =>{

  it("should create a new product and return it", async () =>{
    const req = {
      body:{
        name:"laptop",
        price:50000
      }
    }

    const res = {
      status: vi.fn().mockReturnThis(),
      json: vi.fn()
    }

    vi.spyOn(Product.prototype, "save").mockResolvedValue(req.body);

    await createProduct(req,res);

    expect(res.status).toHaveBeenCalled(201)
    expect(res.json).toHaveBeenCalled(req.body)
  })

  it("should return all products", async () =>{
       const req = {}

       const res = {
        status: vi.fn().mockReturnThis(),
        json: vi.fn()
       }


   vi.spyOn(Product, "find").mockResolvedValue([{name:"laptop", price:50000}])
  await getProducts(req,res);

  expect(res.status).toHaveBeenCalled(200)
  expect(res.json).toHaveBeenCalled([{name:"laptop", price:50000}])
  })

})