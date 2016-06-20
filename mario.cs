using UnityEngine;
using System.Collections;

public class mario : MonoBehaviour {


	public float moveSpeed;
	public float jumpHeight;

	public Transform groundCheck;
	public float groundCheckRadius;
	public LayerMask whatIsGround;
	private bool grounded;

	private bool doubleJumped;

	private Animator anim;

    public Transform firePointRight, firePointLeft;
    public GameObject fireBall;



    // Use this for initialization
    void Start () {
		anim = GetComponent<Animator> ();
	}

	void FixedUpdate() {

		grounded = Physics2D.OverlapCircle (groundCheck.position, groundCheckRadius, whatIsGround);
	}
	
	// Update is called once per frame
	void Update () {
		
		if (grounded)
			doubleJumped = false;

		if (Input.GetKeyDown (KeyCode.W) && grounded) 
		{
			//GetComponent<Rigidbody2D>().velocity = new Vector2 (GetComponent<Rigidbody2D>().velocity.x, jumpHeight);
			Jump();
		}

		if (Input.GetKeyDown (KeyCode.W) && !doubleJumped && !grounded) 
		{
			//GetComponent<Rigidbody2D>().velocity = new Vector2 (GetComponent<Rigidbody2D>().velocity.x, jumpHeight);
			Jump();
			doubleJumped = true;
		}

		if (Input.GetKey (KeyCode.D)) 
		{
			GetComponent<Rigidbody2D> ().velocity = new Vector2 (moveSpeed, GetComponent<Rigidbody2D> ().velocity.y);
			//anim.SetFloat("Speed Right", Mathf.Abs(GetComponent<Rigidbody2D> ().velocity.x));
		}

		if (Input.GetKey (KeyCode.A)) 
		{
			GetComponent<Rigidbody2D> ().velocity = new Vector2 (-moveSpeed, GetComponent<Rigidbody2D> ().velocity.y);
			//anim.SetFloat("Speed Left", Mathf.Abs(GetComponent<Rigidbody2D> ().velocity.x));
		}
		anim.SetFloat("Speed", (GetComponent<Rigidbody2D> ().velocity.x));
        //anim.SetFloat("Speed", 0);

//        if (GetComponent<Rigidbody2D>().velocity.x > 0)
 //           transform.localScale = new Vector3(1f, 1f, 1f);

//        else if (GetComponent<Rigidbody2D>().velocity.x < 0)
  //          transform.localScale = new Vector3(-1f, 1f, 1f);


        if (Input.GetKeyDown(KeyCode.F))
        {
            if (GetComponent<Rigidbody2D>().velocity.x > 0)
                Instantiate(fireBall, firePointRight.position, firePointRight.rotation);
            else if (GetComponent<Rigidbody2D>().velocity.x < 0)
                Instantiate(fireBall, firePointLeft.position, firePointLeft.rotation);



        }

    } 

	public void Jump()
	{
		GetComponent<Rigidbody2D>().velocity = new Vector2 (GetComponent<Rigidbody2D>().velocity.x, jumpHeight);
	}
}
