require "./hello.rb"

describe "hello" do
  it "should generate a greeting" do
    expect(hello("simon")).to eq("hello, simon!")
  end
end
